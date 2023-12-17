// JavaScript code for validating admission form
  document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("admissionForm");

    form.addEventListener("submit", function (event) {
      if (!validateForm()) {
        event.preventDefault();
      }
    });

    function validateForm() {
      var valid = true;

      // Validate Date
      var dateInput = document.getElementById("date");
      if (!isValidDate(dateInput.value)) {
        valid = false;
        alert("Please enter a valid date in YYYY-MM-DD format.");
      }

      // Validate Name
      var nameInput = document.getElementById("name");
      if (nameInput.value.trim() === "") {
        valid = false;
        alert("Name is required.");
      }

      // Validate Contact
      var contactInput = document.getElementById("contact");
      if (!isValidContact(contactInput.value)) {
        valid = false;
        alert("Please enter a valid 10-digit contact number.");
      }

      // Validate Email
      var emailInput = document.getElementById("email");
      if (!isValidEmail(emailInput.value)) {
        valid = false;
        alert("Please enter a valid email address.");
      }

      // Validate Aadhar
      var aadharInput = document.getElementById("aadhar");
      if (!isValidAadhar(aadharInput.value)) {
        valid = false;
        alert("Please enter a valid 12-digit Aadhaar number.");
      }

      // Validate Code
      var codeInput = document.getElementById("code");
      if (!isValidCode(codeInput.value)) {
        valid = false;
        alert("Please enter a valid 10-digit code.");
      }

      return valid;
    }

    function isValidDate(dateString) {
      var regex = /^\d{4}-\d{2}-\d{2}$/;
      return regex.test(dateString);
    }

    function isValidContact(contact) {
      var regex = /^\d{10}$/;
      return regex.test(contact);
    }
        function isValidEmail(email) {
      // You can use a library like validator.js for more complex email validation
      var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return regex.test(email);
    }

    function isValidAadhar(aadhar) {
      var regex = /^\d{12}$/;
      return regex.test(aadhar);
    }

    function isValidCode(code) {
      var regex = /^\d{10}$/;
      return regex.test(code);
    }
  });