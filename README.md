# user_activities

### Requirements

- django==4.1.3
- djangorestframework==3.14.0

### Methods

##### GET /activities/

- list all activities

##### POST /activities/

- create a new activity
  ```
  {
      description*	string
      user*	integer
  }
  ```

##### GET /activities/{id}/

- get activity by id

##### DELETE /activities/{id}/

- delete activity by id
