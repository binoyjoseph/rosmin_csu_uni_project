/*
newsletter.js
Author: Rosmin Roy
Date: 30 May 2026
Description: External JavaScript file for newsletter signup form. 
External Javascript for code reusability and readability.
*/

// Welcome alert shown via the body's onload event in the newsletter HTML page.
function showWelcomeAlert() {
    alert("Welcome to the Verdant Web Solutions Pty Ltd. - Newsletter Signup.");
}

// Does form validation. Returns false to cancel the submission validation fails.
function validateSignupForm(form) {
    // Read the two required name fields from the form element passed in by onsubmit.
    var firstName = form.elements["firstName"].value.trim();
    var lastName = form.elements["lastName"].value.trim();

    // Check First Name
    if (firstName === "") {
        alert("Please enter your First Name. This field is required.");
        form.elements["firstName"].focus();
        // Stop the form from being submitted.
        return false;
    }

    // Check Last Name
    if (lastName === "") {
        alert("Please enter your Last Name. This field is required.");
        form.elements["lastName"].focus();
        return false;
    }

    // Friendly on-screen confirmation when validation passes (per the FAQ in
    // the subject outline: either a pop-up or on-screen notice is acceptable).
    alert("Thank you, " + firstName + "! You are now signed up for the newsletter.");
    return true;
}
