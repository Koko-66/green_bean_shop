//   Code adapted from https://stripe.com/docs/payments/quickstart and CI Boutique Ado walkthrough project

// This is your test publishable API key.
let stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
let clientSecret = $("#id_client_secret").text().slice(1, -1);
let successURL = $("#id_success_url").text().slice(2, -2);
console.log(successURL)
const stripe = Stripe(stripePublicKey);

// initialize();
checkStatus();

document
  .querySelector("#payment-form")
  .addEventListener("submit", handleSubmit);

const appearance = {
  theme: 'stripe',
}
  
// Pass the appearance object to the Elements instance
const elements = stripe.elements({appearance, clientSecret});
let paymentElement = elements.create('payment');
paymentElement.mount('#payment-element');


// Fetches a payment intent and captures the client secret
async function initialize() {
  const response = await fetch("/create-payment-intent", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
  });
  const { clientSecret } = await response.json();

  const appearance = {
    theme: 'stripe',
  };
  elements = stripe.elements({ appearance, clientSecret });

  const paymentElement = elements.create("payment");
  paymentElement.mount("#payment-element");
}


// paymentElement.addEventListener('change', function (event) {
//   let errorDiv = document.getElementById('card-errors');
//   if (event.error) {
//       let html = `
//           <span class="icon" role="alert">
//               <i class="fas fa-times"></i>
//           </span>
//           <span>${event.error.message}</span>
//       `;
//       $(errorDiv).html(html);
//   } else {
//       errorDiv.textContent = '';
//   }
// });


async function handleSubmit(e) {
  e.preventDefault();
  setLoading(true);
  
  // prevent the user from submitting form again
  // by disabling the submit button
  // paymentElement.update({ 'disabled': true }) 
  // $('submit').attr('disabled', true)

  const { error } = await stripe.confirmPayment({
    elements,
    confirmParams: {
      // Make sure to change this to your payment completion page
      return_url: successURL
    },
  });

  // This point will only be reached if there is an immediate error when
  // confirming the payment. Otherwise, your customer will be redirected to
  // your `return_url`. For some payment methods like iDEAL, your customer will
  // be redirected to an intermediate site first to authorize the payment, then
  // redirected to the `return_url`.
  if (error.type === "card_error" || error.type === "validation_error") {
    showMessage(error.message);
    // paymentElement.update({ 'disabled': false }) // enable submit button
    // $('submit-button').attr('disabled', false) // enable submit button

  } else {
    showMessage("An unexpected error occured.");
    // paymentElement.update({ 'disabled': false }) 
  // $('submit').attr('disabled', false)
  }

  setLoading(false);
}

// Fetches the payment intent status after payment submission
async function checkStatus() {
  const clientSecret = new URLSearchParams(window.location.search).get(
    "payment_intent_client_secret"
  );

  if (!clientSecret) {
    return;
  }

  const { paymentIntent } = await stripe.retrievePaymentIntent(clientSecret);

  switch (paymentIntent.status) {
    case "succeeded":
      showMessage("Payment succeeded!");
      break;
    case "processing":
      showMessage("Your payment is processing.");
      break;
    case "requires_payment_method":
      showMessage("Your payment was not successful, please try again.");
      break;
    default:
      showMessage("Something went wrong.");
      break;
  }
}

// ------- UI helpers -------

function showMessage(messageText) {
  const messageContainer = document.querySelector("#payment-message");

  messageContainer.classList.remove("hidden");
  messageContainer.textContent = messageText;

  setTimeout(function () {
    messageContainer.classList.add("hidden");
    messageText.textContent = "";
  }, 4000);
}

// Show a spinner on payment submission
function setLoading(isLoading) {
  if (isLoading) {
    // Disable the button and show a spinner
    document.querySelector("#submit").disabled = true;
    document.querySelector("#spinner").classList.remove("hidden");
    document.querySelector("#button-text").classList.add("hidden");
  } else {
    document.querySelector("#submit").disabled = false;
    document.querySelector("#spinner").classList.add("hidden");
    document.querySelector("#button-text").classList.remove("hidden");
  }
}