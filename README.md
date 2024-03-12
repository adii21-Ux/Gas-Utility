# Gas Utility Customer Service Application
This Django application provides customer service functionalities for a gas utility company. It allows customers to submit service requests, track their status, and manage their account information. Additionally, representatives can manage service requests and provide support to customers.

## Endpoints
### Authentication
1. Register Customer: /register/customer/
- Allows customers to register for an account.
- Access: Navigate to the registration page and fill out the registration form.

2. Register Representative: /register/representative/
- Allows representatives to register for an account.
- Access: Navigate to the registration page and fill out the registration form.
  
3. Login: /login/
- Allows users to log in to their accounts.
- Access: Navigate to the login page and enter your credentials.

4. Logout: /logout/
- Allows logged-in users to log out of their accounts.
- Access: Click on the logout button while logged in.

6. User Profile: /profile/
- Displays the profile information of the logged-in user.
- Access: Requires user authentication.
- Service Requests

7. Create Service Request: /create/
- Allows customers to submit a new service request.
- Access: Requires user authentication.

7. User Service Requests: /service-requests/
- Displays a list of service requests submitted by the logged-in customer.
- Access: Requires user authentication.

8. Service Request Details: /service-requests/<int:request_id>/
- Displays detailed information about a specific service request.
- Access: Requires user authentication.
- Representative Dashboard

9. All Service Requests: /all-service-requests/
- Displays a list of all service requests for representatives.
- Access: Requires representative authentication.

10. Update Service Request: /update_service_request/<int:request_id>/
- Allows representatives to update the status of a service request.
- Access: Requires representative authentication.

11. Update Resolved At: /update_resolved_at/<int:request_id>/
- Allows representatives to update the resolved date and time of a service request.
- Access: Requires representative authentication.
