var ldap = require('ldapjs')
var express = require('express')
var client = ldap.createClient({
  url: 'ldap://ldap.andrew.cmu.edu'
})
// ldap.cmu.edu


var app = express()



var search = function (andrewId, callback) {
  var options = {
    filter: `(cmuAndrewID=${andrewId})`,
    scope: 'sub'
  };

  client.search('ou=person, dc=cmu, dc=edu', options, function (err, searchStream) {
    if (err){ callback(err); return }
    var results = [];

    searchStream.on('searchEntry', function (entry) {
      results.push(entry.object)
    })
    searchStream.on('error', function (err) {
      callback(err)
    })
    searchStream.on('end', function (result) {
      callback(null, results)
    })
  })
}

app.get('/andrewId/:id', function (req, res) {
  search (req.params.id, function (err, response) {
    if (err) {
      res.status(500)
      res.end(JSON.stringify(err))
      return
    }
  res.end(JSON.stringify(response))
  })
})

app.listen(8080)
