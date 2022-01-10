# This script reads in a file of users in an XML file.
# It then uses that file to create correct Active directory Users,
# OUs and user information.


# Get the root domain, use it to build a path.
$getDomain = Get-ADForest
$dString = $getDomain.Name.toString()
$pathString = $dString.split('.')

foreach ($p in $pathString) {
    $dpath += "DC=$p,"
}
$dpath = $dpath.Trim(',')


# Prompt the user for the location of the XML file
Write-Host "Filepath to XML document:"
$pathToFile = Read-Host -Prompt ">"

# Insure the file is valid
If ($null -eq $pathToFile) { Write-Host 'You must provide a valid filepath' }

Try { [xml]$userdoc = Get-Content $pathToFile -ErrorAction Stop }
Catch {
    Write-Host 'Filepath is invalid or file is an invalid type.'
    write-host 'Check for typos and try again.'; exit;
}


# Loop through each user. If the OU does not exist then build it.
ForEach ($i in $userdoc.root.user) {
    $OU = $i.ou;
    Try {
        $testOU = Get-ADOrganizationalUnit -Filter "Name -eq '$OU'" -ErrorAction Stop 
        if ($testOU) { Write-Host "OU $OU found." }
        else {
            Write-Host "OU does not exist. Creating OU $OU" -ForegroundColor Yellow;
            New-ADOrganizationalUnit $OU -path "$dpath" -ProtectedFromAccidentalDeletion $false
        }
    }
    Catch {
        Write-Host "OU does not exist. Creating OU $OU";
        New-ADOrganizationalUnit $OU -path "$dpath" -ProtectedFromAccidentalDeletion $false
    }
    
    # While this does use a secure string, it is not being given an encrypted string.
    # It would be best if the passwords were saved as encrypted strings, but this is just an example
    $fullname = $i.firstname + " " + $i.lastname
    $SecPass = ConvertTo-SecureString $i.password -AsPlainText -Force
    Write-Host "Adding User $fullname" -ForegroundColor Green



    # This creates the users, and if applicable will set their manager as well.
    if ($i.manager) {
        New-ADUser -Name $i.account -UserPrincipalName $i.account `
            -GivenName $i.firstname -Surname $i.lastname `
            -DisplayName $fullname -SamAccountName $i.account `
            -AccountPassword $SecPass -ChangePasswordAtLogon $true `
            -path "OU=$OU,$dpath" -Enabled $true `
            -Manager $i.manager -Description $i.description
    }
    else {
        New-ADUser -Name $i.account -UserPrincipalName $i.account `
            -GivenName $i.firstname -Surname $i.lastname `
            -DisplayName $fullname -SamAccountName $i.account `
            -AccountPassword $SecPass -ChangePasswordAtLogon $true `
            -path "OU=$OU,$dpath" -Enabled $true `
            -Description $i.description
    }


    # This block handles the creation and setting of groups.
    $XMLgroup = $i.memberOf.group
    ForEach ($g in $XMLgroup) {
        Try {
            $testGroup = Get-ADGroup -Filter "Name -eq '$g'" -ErrorAction Stop
            if ($testGroup) {
                Write-Host "Group $g Found. Adding $fullname to Group $g" 
            }
            else {
                Write-Host "Group $g does not exist. Creating $g and adding $fullname" -ForegroundColor Yellow;
                New-ADGroup -DisplayName "$g" -Path "OU=$OU,$dpath" `
                    -GroupCategory Security -Name "$g" -GroupScope global
            }
        }
        Catch {
            Write-Host "Group $g does not exist. Creating $g" -ForegroundColor Yellow;
            New-ADGroup -DisplayName "$g" -Path "OU=$OU,$dpath" `
                -GroupCategory Security -Name "$g" -GroupScope global
        }
        Add-ADGroupMember -Identity $g -Members $i.account
    }
    Write-Host "Operations on $fullname are complete."
}
Write-Host "File read complete."