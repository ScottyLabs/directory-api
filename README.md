# directory-api
The Directory API has endpoints allowing you to get information about Carnegie Mellon AndrewIDs. You can query to check if an AndrewID exists, and to get some basic information about a person given their AndrewID. Our information comes from the public LDAP servers run by Carnegie Mellon, which are the backing agent for the Andrew directory.

Try it at :  apis.scottylabs.org/directory/v1/andrewID/odb/


## Installation
```
npm install
```
## How to Use

In version 1, we have two endpoints, one at /andrewID/:id and one at /andrewID/:id/raw. The former has several fields we prefill from the LDAP data for your convenience. You can check for AndrewID existence by noting that requesting a nonexistent AndrewID will return a 404: Not Found status. The second endpoint is for those of you who want access to the raw LDAP data, which has more data but much less structure between people.


### Endpoint 1
Sample Request:
```GET https://apis.scottylabs.org/directory/v1/andrewID/odb```

Sample Format:
 ```
 {
  "andrewID": string,
  "first_name": string,
  "middle_name": string,
  "last_name": string,
  "preferred_email": string,
  "campus": string,
  "department": string,
  "affiliation": string,
  "names": [string],

  // This may or may not be in the query, depending on if it makes sense.
  "student_level": string,
  "student_class" string,
  "job_title": string,
  "office": string,
}
```
### Endpoint 2

Sample Request:

```GET https://apis.scottylabs.org/directory/v1/andrewID/odb/raw```

Sample Response:
```
{
  "dn": "guid=A9C831E4-66C8-11E2-8000-00144F799A7A,ou=PERSON,dc=CMU,dc=EDU",
  "controls": [],
  "cmuCampus": "Pittsburgh",
  "cmuDepartment": "Computer Science",
  "cmuMiddleName": "D",
  "cmuPersonAffiliation": "Student",
  "cmuPrimaryCampus": "Pittsburgh",
  "cmuPrivate": [
    "homePhone",
    "homePostalAddress",
    "postalAddress",
    "telephoneNumber"
  ],
  "cmuStudentLevel": "Undergrad",
  "cn": [
    "Oscar Bezi",
    "Oscar D Bezi"
  ],
  "eduPersonAffiliation": "Student",
  "eduPersonPrimaryAffiliation": "Student",
  "eduPersonSchoolCollegeName": [
    "School of Computer Science",
    "Student Employment"
  ],
  "givenName": "Oscar",
  "guid": "A9C831E4-66C8-11E2-8000-00144F799A7A",
  "objectClass": "cmuPerson",
  "sn": "Bezi",
  "cmuAndrewCommonNamespaceId": "odb",
  "cmuAccount": [
    "uid=odb,ou=account,dc=andrew,dc=cmu,dc=edu",
    "uid=bezi,ou=account,dc=cmu,dc=edu"
  ],
  "cmuAndrewId": "odb",
  "cmuActiveDN": [
    "uid=odb,ou=account,dc=andrew,dc=cmu,dc=edu",
    "uid=bezi,ou=account,dc=cmu,dc=edu"
  ],
  "cmuPersonPrincipalName": "odb@ANDREW.CMU.EDU",
  "cmueduId": "bezi",
  "mail": "bezi@cmu.edu",
  "cmuPreferredMail": "bezi@cmu.edu",
  "title": "Job Mgmt Student Job Profile",
  "cmuStudentClass": "Junior"
}
```

## Contributing to the api
1. Make an issue explaining what you're trying to do.
2. Work on a commit on a fork of this repo.
3. Submit a pull request referencing the original issue.

You don't have to pick from existing issues, feel free to make new ones to work on.

Happy coding

