// function in số chẵn

function getEvenNumber(number) {
    for (let index = 0; index < number; index++) {
        if (index % 2 == 0) {
            console.log(index);
        }
    }
}

getEvenNumber(20);

let currentTime = new Date();
let hour = currentTime.getHours();
let minute = currentTime.getMinutes();
let second = currentTime.getSeconds();

let clock = document.getElementById("clock");
clock.innerHTML = hour + ":" + minute + ":" + second;
