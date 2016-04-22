/* @file server.js
 * @brief The entire logic for the Directory API, which is just a thin shim
 * around CMU LDAP.
 *
 * @author Shalom Yiblet (shalom@scottylabs)
 * @author Oscar Bezi (bezi@scottylabs)
 */
'use strict';

// =============================================================================
// Config
// =============================================================================
/* @brief URL of the CMU LDAP server. */
var ldapURL = 'ldap://ldap.andrew.cmu.edu';

/* @brief The port to listen on. */
var port = 8080;

/* @brief Returned on 500 err codes. */
var errString = 'Something went wrong.';

// =============================================================================
// LDAP
// =============================================================================
var ldap = require('ldapjs');

var client = ldap.createClient({
  url: ldapURL,
});

// =============================================================================
//  Express
// =============================================================================
var express = require('express');
var morgan = require('morgan');

var app = express();
app.use(morgan('combined'));

// =============================================================================
// Some helper functions.
// =============================================================================

/* @brief Nice date format for startup time. */
var dateFormat = require('dateformat');

/* @brief Searches for an AndrewID using LDAP.
 * @param String andrewID The AndrewID to look for.
 * @param Function callback The callback.
 */
var search = function (andrewId, callback) {
  var options = {
    filter: `(cmuAndrewID=${andrewId})`,
    scope: 'sub',
  };

  client.search('ou=person, dc=cmu, dc=edu', options, function (err, str) {
    if (err) { callback(err); return; }

    var results = [];

    str.on('searchEntry', function (entry) {
      results.push(entry.object);
    });

    str.on('error', function (e) {
      callback(e);
    });

    str.on('end', function () {
      callback(null, results);
    });
  });
};

/* @brief Error checking middleware that's the same for both endpoints.  */
var errCheck = function (req, res, next) {
  search (req.params.id, function (err, response) {
    if (err) {
      res.status(500);
      res.end(errString);
      return;
    }

    if (response.length > 1) {
      res.status(500);
      res.end(errString);
      return;
    }

    if (response.length === 0) {
      res.status(404);
      res.end('Person not found.');
      return;
    }

    var raw = response[0];
    req.rawData = raw;
    next();
  });
};

// =============================================================================
// Routes.
// =============================================================================
app.get('/andrewId/:id/raw', errCheck, function (req, res) {
  res.json(req.rawData);
});

app.get('/andrewId/:id', errCheck, function (req, res) {
  var raw = req.rawData;

  var department = Array.isArray(raw.cmuDepartment)
    ? raw.cmuDepartment
    : [raw.cmuDepartment];

  var person = {
    // All requests will have these fields.
    andrewID: raw.cmuAndrewId,

    first_name: raw.givenName,
    middle_name: raw.cmuMiddleName,
    last_name: raw.sn,

    preferred_email: raw.mail,

    // This may or may not be in the query.
    campus: raw.cmuCampus,
    department: department,
    affiliation: raw.eduPersonPrimaryAffiliation,
    student_level: raw.cmuStudentLevel,
    student_class: raw.cmuStudentClass,
    names: raw.cn,
    job_title: raw.title,
    office: raw.postalAddress,
  };

  res.json(person);
});

// Start up the server.
app.listen(port,
  () => {
    var now = dateFormat(new Date (), "dddd, mmmm dS, yyyy, h:MM:ss TT");
    console.log(`Directory API up and running on port ${ port }: ${ now }.`)
  }
);
