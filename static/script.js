$(document).ready(function () {

    $("#predictForm").submit(function (e) {

        e.preventDefault();

        $("#predictBtn")
            .html("⏳ Predicting...")
            .prop("disabled", true);

        $("#prediction").hide();

        $.ajax({

            url: "/predict",

            type: "POST",

            data: $(this).serialize(),

            success: function (result) {

                let price = Number(result);

                let lakh = (price / 100000).toFixed(2);

                $("#prediction").html(`

                    <div class="result-card">

                        <h2>💰 Estimated Car Price</h2>

                        <h1>₹ ${price.toLocaleString('en-IN',{
                            maximumFractionDigits:2
                        })}</h1>

                        <p>Approx. ₹ ${lakh} Lakhs</p>

                    </div>

                `);

                $("#prediction").fadeIn(500);

                $("#predictBtn")
                    .html("🚀 Predict Again")
                    .prop("disabled", false);

            },

            error: function () {

                $("#prediction").html(`

                    <div class="result-card">

                        <h2 style="color:red;">❌ Prediction Failed</h2>

                        <p>Please try again.</p>

                    </div>

                `);

                $("#prediction").fadeIn();

                $("#predictBtn")
                    .html("🚀 Predict Car Price")
                    .prop("disabled", false);

            }

        });

    });

});