let navbarItems = ["Home", "About", "Shop", "Donate", "Contact"];

let query = "";

for (let index = 0; index < navbarItems.length; index++) {
    let element = navbarItems[index];
    query = query + `<div class="navbar-item">${element}</div>`;
}

let a = (document.querySelector(".navbar").innerHTML = query);
