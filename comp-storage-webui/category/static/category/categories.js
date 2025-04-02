document.addEventListener('DOMContentLoaded', function() {
    const selectElement = document.getElementById('parents'); // Select element (hidden element containing all options)
    const inactiveDiv = document.getElementById('parents-div-inactive'); // Div for inactive options
    const activeDiv = document.getElementById('parents-div-active'); // Div for active options
    const searchInput = document.getElementById('search'); // Search input field
    const addButton = document.getElementById('add-category'); // Button to add new entry

    /*
    * This function updates the active and inactive options displayed in the respective divs.
    * It filters the options based on their selected status and creates new div elements for each option.
    * The active options are displayed in the activeDiv and the inactive options in the inactiveDiv.
    * It also clears the innerHTML of both divs before appending the new elements.
    * The function is called initially to populate the divs with the current options.
    */
    function updateSelectedOptions() {
        
        // Clear the innerHTML of both divs before updating
        activeDiv.innerHTML = '';
        inactiveDiv.innerHTML = '';
        
        const options = Array.from(selectElement.options); // Get all options from the select element

        options.forEach(option => {
            const newButton = document.createElement('div'); // Create a new div element for each option
            newButton.textContent = option.textContent; // Set the text content of the div to the option's text
            newButton.classList.add('btn', 'btn-outline-secondary', 'tag'); // Add classes to the div

            // Check if the option is selected and append it to the respective div
            if (option.selected) {
                newButton.classList.add('active'); // Add 'active' class for selected options
                activeDiv.appendChild(newButton); // Append to activeDiv
            } else {
                inactiveDiv.appendChild(newButton); // Append to inactiveDiv
            }
        });
    }

    /*
    * This function handles the click event on the inactive options.
    * When an inactive option is clicked, it becomes active (selected) and the updateSelectedOptions function is called to refresh the display.
    */
    addButton.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default action of the button click
        // Check if the search input field is empty
        if (searchInput.value.trim() === '') {
            return; // Exit the function if the input is empty
        }

        // Get the value from the search input field and trim any whitespace
        const newValue = searchInput.value.trim();
        searchInput.value = ''; // Clear the search input field
        if (newValue) { // Check if the input is not empty
            // Check if the input value is already present in the select element
            const existingOption = Array.from(selectElement.options).find(option => option.value === newValue);
            if (existingOption) {
                // Add the category to the select element if it doesn't exist
                existingOption.selected = true; // Set the option as selected
                updateSelectedOptions(); // Update the displayed options
                return; // Exit the function if it exists
            }
            // POST request to add the new category
            const url = addButton.getAttribute('data-url'); // Get the URL from the button's data attribute

            const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value; // Get the CSRF token
            const data = new FormData(); // Create a new FormData object
            data.append('name', newValue); // Append the new category name to the FormData object
            data.append('csrfmiddlewaretoken', csrfToken); // Append the CSRF token


            fetch(url, {
                method: 'POST', // Set the request method to POST
                body: data, // Set the request body to the FormData object
            })
            .then(response => {
                if (!response.ok) { // Check if the response is not OK
                    throw new Error('Network response was not ok'); // Throw an error if the response is not OK
                }
                return response.json(); // Parse the response as JSON
            })
            

            // Create a new option element and set its properties
            const newOption = document.createElement('option');
            newOption.value = newValue;
            newOption.selected = true;
            newOption.textContent = newValue;
            selectElement.appendChild(newOption);
            updateSelectedOptions();
        }
    });

    searchInput.addEventListener('input', function() {
        const filter = searchInput.value.toLowerCase();
        // Filter the active and inactive options based on the search input
        Array.from(activeDiv.children).forEach(option => {
            if (option.textContent.toLowerCase().includes(filter)) {
                option.style.display = '';
            } else {
                option.style.display = 'none';
            }
        });
        // Filter the inactive options based on the search input
        Array.from(inactiveDiv.children).forEach(option => {
            if (option.textContent.toLowerCase().includes(filter)) {
                option.style.display = '';
            } else {
                option.style.display = 'none';
            }
        });
    });

    // If user presses enter in the search input, add the new entry
    searchInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') { // Check if the pressed key is 'Enter'
            event.preventDefault(); // Prevent the default action of the Enter key
            addButton.click(); // Trigger the click event on the add entry button
        }
    });

    function tag(event, enabled) {
        const clickedOption = event.target; // Get the clicked option
        const optionValue = clickedOption.textContent; // Get the value of the clicked option

        // Find the corresponding option in the select element and set it as selected or unselected
        const correspondingOption = Array.from(selectElement.options).find(option => option.textContent === optionValue);
        if (correspondingOption) {
            correspondingOption.selected = enabled; // Set the option as selected or unselected
            updateSelectedOptions(); // Update the displayed options
        }
    }

    // Function to remove an active option when clicked
    function disableTag(event) { tag(event, false); }
    // Function to add an inactive option when clicked
    function enableTag(event) { tag(event, true); }

    // Add event listeners to the inactive and active divs for click events
    inactiveDiv.addEventListener('click', enableTag); // Call enableTag when an inactive option is clicked
    activeDiv.addEventListener('click', disableTag); // Call disableTag when an active option is clicked


    updateSelectedOptions();
});