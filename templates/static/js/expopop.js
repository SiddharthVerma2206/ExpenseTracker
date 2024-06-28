function displayDiv() {
    var typeOfAcc = document.getElementById('typeofacc').value;

    // Show the corresponding div based on selection
    if (typeOfAcc === 'Credit Card') {
        document.getElementById('limit-field').classList.remove('hidden');
        document.getElementById('amount-field').classList.add('hidden');
    } else if (typeOfAcc === 'Cash') {
        document.getElementById('limit-field').classList.add('hidden');
        document.getElementById('amount-field').classList.remove('hidden');
    } else if (typeOfAcc === 'Bank Account') {
        document.getElementById('limit-field').classList.add('hidden');
        document.getElementById('amount-field').classList.remove('hidden');
    }
}

function popupFn() {
    document.getElementById("overlay").style.display = "block";
    document.getElementById("popupDialog").style.display = "block";
}

function closeFn() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("popupDialog").style.display = "none";
}

document.getElementById("overlay").addEventListener("click", function() {
    closeFn();
});
