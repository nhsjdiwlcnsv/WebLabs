// Данные о пассажирах (ассоциативный массив)
let passengers = [
    { "lastName": "Aboba", "firstName": "Ayops", "middleName": "Aboben", "rid": 123 },
    { "lastName": "Aboba", "firstName": "Abliba", "middleName": "Ahuhskin", "rid": 456 },
    { "lastName": "Ahuha", "firstName": "Amoga", "middleName": "Amoger", "rid": 789 },
];

function searchPassengers() {
    let lastName = document.getElementById('lastName').value;
    let matchingPassengers = [];

    for (let i = 0; i < passengers.length; i++) {
        if (passengers[i]["lastName"].toLowerCase() === lastName.toLowerCase()) {
            matchingPassengers.push(passengers[i]);
        }
    }

    displayResult(matchingPassengers);
}

function displayResult(matchingPassengers) {
    let resultContainer = document.getElementById('result');
    resultContainer.innerHTML = '';

    if (matchingPassengers.length > 0) {
        resultContainer.innerHTML = '<h3>Найдены однофамильцы:</h3>';
        for (let i = 0; i < matchingPassengers.length; i++) {
            let passengerInfo = matchingPassengers[i];
            resultContainer.innerHTML += '<p>' + passengerInfo["lastName"] + ' ' +
                passengerInfo["firstName"] + ' ' + passengerInfo["middleName"] + '</p>';
        }
    } else {
        resultContainer.innerHTML = '<p>No people with equal last names detected.</p>';
    }
}