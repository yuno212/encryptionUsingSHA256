function checkoutPlan(plan){
  let id = 1;
  if(plan == 'starter'){id=1}
  if(plan == 'basic'){id=2}
  if(plan == 'advanced'){id=3}
  if(plan == 'ultimate'){id=4}
  if(plan == 'custom'){id=5}
  fetch("/create-checkout-session", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      items: [
        { id: id, quantity: 1 },
      ],
    }),
  })
    .then(res => {
      if (res.ok) return res.json()
      return res.json().then(json => Promise.reject(json))
    })
    .then(({ url }) => {
      window.location = url
    })
    .catch(e => {
      console.error(e.error)
    })
}
