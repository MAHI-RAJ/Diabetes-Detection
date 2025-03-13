
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form"); 
    const inputs = document.querySelectorAll("input"); 

   
    loadFormData();

    // Event listener for form submission
    form.addEventListener("submit", function (event) {
        event.preventDefault(); 

        let formData = {};

        inputs.forEach((input) => {
            formData[input.name] = input.value;
        });

       
        localStorage.setItem("formData", JSON.stringify(formData));

        // Show success message
        alert("Data saved successfully! ✅");

       ;
    });

    
    function loadFormData() {
        let savedData = localStorage.getItem("formData");

        if (savedData) {
            savedData = JSON.parse(savedData);

            // Populate form inputs with saved data
            inputs.forEach((input) => {
                if (savedData[input.name]) {
                    input.value = savedData[input.name];
                }
            });
        }
    }
});
