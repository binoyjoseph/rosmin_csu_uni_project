/*
newsletter.js
Author: Rosmin Roy
Date: 30 May 2026
Description:
    External JavaScript file for the Verdant Web Solutions newsletter signup form.
    Kept external (not inline) for code reusability and readability, so the same
    behaviour can be attached to any future signup page just by linking this file.
    - showWelcomeAlert(): displays the welcome alert when the signup page loads.
    - validateSignupForm(): verifies the First Name and Last Name fields are not
      empty on submit. If either is empty, an alert is shown and the form is
      prevented from being sent to the server.
*/

// Welcome alert shown via the body's onload event in the signup HTML page.
function showWelcomeAlert() {
    alert("Welcome to the Verdant Web Solutions Pty Ltd. - Newsletter Signup");
}

// Submit-time validation. Returns false to cancel the submission if either
// of the required name fields is empty (after trimming whitespace).
function validateSignupForm(form) {
    // Read the two required name fields from the form element passed in by onsubmit.
    var firstName = form.firstName.value.trim();
    var lastName = form.lastName.value.trim();

    // Check First Name
    if (firstName === "") {
        alert("Please enter your First Name. This field is required.");
        form.firstName.focus();
        return false; // Stop the form from being submitted.
    }

    // Check Last Name
    if (lastName === "") {
        alert("Please enter your Last Name. This field is required.");
        form.lastName.focus();
        return false; // Stop the form from being submitted.
    }

    // Friendly on-screen confirmation when validation passes (per the FAQ in
    // the subject outline: either a pop-up or on-screen notice is acceptable).
    alert("Thank you, " + firstName + "! You are now signed up for the newsletter.");
    return true;
}
