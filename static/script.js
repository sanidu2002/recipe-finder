function searchRecipe(){

let ingredient = document.getElementById("ingredient").value;

fetch(`/search?ingredient=${ingredient}`)
.then(res => res.json())
.then(data => {

let results = document.getElementById("results");
results.innerHTML = "";

if(data.meals){

data.meals.forEach(meal => {

results.innerHTML += `
<div class="card">
<img src="${meal.strMealThumb}">
<h3>${meal.strMeal}</h3>
<button class="favorite-btn" onclick="saveFavorite('${meal.strMeal}')">
⭐ Save
</button>
</div>
`;

});

}

});

}

function saveFavorite(name){

fetch('/favorite',{
method:'POST',
headers:{
'Content-Type':'application/json'
},
body:JSON.stringify({
name:name,
instructions:"Recipe saved"
})
})
.then(res=>res.json())
.then(data=>{
alert("Saved to favorites!");
});

}

function showFavorites(){

fetch('/favorites')
.then(res => res.json())
.then(data => {

let results = document.getElementById("results");

results.innerHTML = "<h2>⭐ Favorite Recipes</h2>";

let list = "<ul>";

data.forEach(recipe => {

list += `<li>${recipe[0]}</li>`;

});

list += "</ul>";

results.innerHTML += list;

});

}