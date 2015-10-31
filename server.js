var ldap = require('ldapjs')

// ldap.cmu.edu


var client = ldap.createClient({
  url: 'ldap://ldap.andrew.cmu.edu'
})

var empty = {
  filter: '(cmuAndrewID=syiblet)',
  scope: "sub"
}

client.search('ou=person, dc=cmu, dc=edu', empty, function (err, result) {
  result.on('searchEntry', function (entry) {
    console.log('entry: ' + JSON.stringify(entry.object))
  })
  result.on('searchReference', function (referral) {
    console.log('referral: ' + referral.uris.join())
  })
  result.on('error', function (err) {
    console.error('error: ' + err.message)
  })
  result.on('end', function (result) {
    console.log('status: ' + result.status)
  })
})
