require("dotenv").config()

const express = require("express")
const app = express()
const port = process.env.PORT || 5000
app.use(express.json())
app.use(express.static("public"))
const stripe = require("stripe")(process.env.STRIPE_PRIVATE_KEY)


const availableItems = new Map([
    [1, {   priceInCents: 9999, name : "Starter Plan"}],
    [2, {   priceInCents: 24999, name : "Basic Plan"}],
    [3, {   priceInCents: 39999, name : "Advanced Plan"}],
    [4, {   priceInCents: 99999, name : "Ultimate Plan"}],
    [5, {   priceInCents: 199999, name: "Custom Plan"}],
])

app.post("/create-checkout-session", async (req, res) => {
    try {
      const session = await stripe.checkout.sessions.create({
        payment_method_types: ["card"],
        mode: "payment",
        line_items: req.body.items.map(item => {
          const storeItem = availableItems.get(item.id)
          return {
            price_data: {
              currency: "usd",
              product_data: {
                name: storeItem.name,
              },
              unit_amount: storeItem.priceInCents,
            },
            quantity: item.quantity,
          }
        }),
        success_url: `${process.env.SERVER_URL}success?session_id={CHECKOUT_SESSION_ID}`,
        cancel_url: `${process.env.SERVER_URL}`,
      })
      res.json({ url: session.url })
    } catch (e) {
      res.status(500).json({ error: e.message })
    }
  })

function findProductName(map, price){
  for(let i = 1; i < 6; i++){
    if(map.get(i)['priceInCents'] == price){
      return(i)
    }
  }
}

// This example sets up an endpoint using the Express framework.
app.get('/', function (req, res) {
  res.render('index', {});
});


app.get('/success', async (req, res) => {
  const session = await stripe.checkout.sessions.retrieve(req.query.session_id);
  const customer = await stripe.customers.retrieve(session.customer);
  const subtotal = session.amount_subtotal;
  const product = availableItems.get(findProductName(availableItems, subtotal))['name'];

  res.send(`<html><body><h1>Thanks for your order, ${customer.name} for ordering ${product}!</h1><p>Your customer ID is : ${session.customer}</p></body></html>`);
  console.log(session)
  console.log(customer)
});

app.listen(port, () => console.log(`Listening on port ${port}!`));
