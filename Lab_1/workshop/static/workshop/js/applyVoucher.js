const voucherInput = document.getElementById("voucher-input")
const serviceInput = document.getElementById("service-input")
const submitButton = document.getElementById('apply-voucher');
const newPrice = document.getElementById('new-price');
const oldPrice = document.getElementById('old-price');
const voucherName = document.getElementById('voucher-name');

submitButton.addEventListener('click', (event) => {
    event.preventDefault(); // Предотвратить отправку формы

    const voucher = voucherInput.value;
    const service = serviceInput.value;

    fetch('http://127.0.0.1:8000/apply-voucher/', {
        method: 'POST',
        body: JSON.stringify({ voucher: voucher, service: service }),
        headers: {'Content-Type': 'application/json',},
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            newPrice.textContent = `${data.newPrice}`;
            oldPrice.textContent = `${data.oldPrice}`;
            voucherName.textContent = `${data.voucherTitle}`;
        } else {
            alert('Invalid voucher applied!');
        }
    })
    .catch((error) => console.log('Caught error:', error));
});