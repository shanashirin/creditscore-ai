async function predictRisk(){

let age=document.getElementById("age").value;
let amount=document.getElementById("amount").value;
let duration=document.getElementById("duration").value;

const response=await fetch("/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
Age:parseInt(age),
CreditAmount:parseFloat(amount),
Duration:parseInt(duration)
})

});

const data=await response.json();

document.getElementById("result").innerHTML=
`
<h2>${data.risk}</h2>
<p>Probability : ${data.probability}%</p>
`;

}