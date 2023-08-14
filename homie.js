// Get the chat container element


// Function to handle user input and send it to the chatbot
async function handleUserInput() {
  const userInput = document.getElementById('user-input').value;
  displayMessage(userInput, true);



  // Parse the response as JSON
  const responseData = await response.json();

  // Extract the chatbot response from the JSON data
  const chatbotResponse = responseData.response;

  // Display the chatbot response in the chat window
  displayMessage(chatbotResponse);

  // Clear the user input
  document.getElementById('user-input').value = '';
}

  // Send the user input to the server for processing
  const response = await fetch('/chatbot', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ text: userInput }),
  });









const hiddenElements=document.querySelectorAll('.hidden');
hiddenElements.forEach((el)=> observer.observe(el));


// Check if the browser supports the Notification API
if ("Notification" in window) {
    // Request permission from the user to display notifications
    Notification.requestPermission()
      .then(permission => {
        if (permission === "granted") {
          // Create a new notification
          new Notification("u have updated the website!");
        }
      })
      .catch(err => {
        console.error("Notification request error:", err);
      });
  }
  