// The code for this js file is taken from the Boutique Ado student tutorial
// project by the Code Institute, with very minor edits.

// Add event listener
document.addEventListener('DOMContentLoaded', function () {
    let stripePublicKey = $('#id_stripe_public_key').text(). slice(1, -1);
    let clientSecret = $('#id_client_secret').text(). slice(1, -1);
    let stripe = Stripe(stripePublicKey);
    let elements = stripe.elements();

    // Styling for the card element
    let style = {
        base: {
            color: '#000',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };

    // Create card element with the styling above
    let card = elements.create('card', {style: style});
    card.mount('#card-element');

    // Handle realtime validation errors on the card element
    card.addEventListener('change', function (event) {
        var errorDiv = $('#card-errors');
        if (event.error) {
            var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            `;
            $(errorDiv).html(html);
        } else {
            errorDiv.textContent = '';
        }
    });


    // Handle realtime validation errors on the card element
    card.addEventListener('change', function (event) {
        var errorDiv = document.getElementById('card-errors');
        if (event.error) {
            var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            `;
            $(errorDiv).html(html);
        } else {
            errorDiv.textContent = '';
        }
    });

    // Handle form submit
    var form = document.getElementById('adoption-form');

    // Wait with submitting the form until Stripe confirms payment as successful
    form.addEventListener('submit', function(ev) {
        ev.preventDefault();
        card.update({ 'disabled': true});
        $('#submit-button').attr('disabled', true);
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
            }
        }).then(function(result) {
            if (result.error) { // display errors if Stripe finds any
                var errorDiv = $('#card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                card.update({'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {      // Update payment intent id with the newest version of it and submit the form
                if (result.paymentIntent.status === 'succeeded') {
                    $('input[name="payment_intent_id"]').val(result.paymentIntent.id);
                    form.submit();
                }
            }
        });
    });
});