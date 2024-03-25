document.getElementById('displayResult').value = 0;

document.addEventListener('DOMContentLoaded', function () {
    const display = document.getElementById('displayResult');
    let currentOperation = "";
    let firstInput = "";
    let operator = "";
    let secondInput = "";
    let calculationDone = false;

    document.querySelectorAll('.number').forEach(button => {
        button.addEventListener('click', handleNumberClick);
    });

    document.querySelectorAll('.operator').forEach(button => {
        button.addEventListener('click', handleOperatorClick);
    });

    document.getElementById('clear').addEventListener('click', clearAll);

    document.addEventListener('keyup', function (e) {
        if (!isNaN(e.key) || e.key === ".") {
            handleNumberClick({ target: { innerText: e.key } });
        } else if (["+", "-", "x", "/", "="].includes(e.key) || e.key === "Enter") {
            if (e.key === "Enter") {
                handleOperatorClick({ target: { innerText: "=" } });
            } else {
                handleOperatorClick({ target: { innerText: e.key } });
            }
        } else if (e.key === "Backspace" || e.key === "Escape") {
            clearAll();
        }
    });

    function handleNumberClick(e) {
        if (calculationDone) {
            clearAll();
            calculationDone = false;
        }
        
        if (!operator) {
            firstInput += e.target.innerText;
        } else {
            secondInput += e.target.innerText;
        }
        currentOperation += e.target.innerText;
        display.value = currentOperation;
    }

    function handleOperatorClick(e) {
        if (e.target.innerText === "=" || e.target.innerText === "Enter") {
            if (firstInput && operator && secondInput) {
                let result = operate(firstInput, secondInput, operator);
                display.value = result;
                firstInput = result;
                secondInput = "";
                operator = "";
                calculationDone = true;
            }
        } else {
            if (!firstInput) {
                return;
            }
            if (firstInput && secondInput && operator) {
                let result = operate(firstInput, secondInput, operator);
                firstInput = result;
                secondInput = "";
                currentOperation = result;
            }
            operator = e.target.innerText;
            currentOperation += ` ${operator} `;
            display.value = currentOperation;
        }
    }

    function operate(a, b, operation) {
        a = parseFloat(a);
        b = parseFloat(b);
        let result;

        switch (operation) {
            case '+':
                result = a + b;
                break;
            case '-':
                result = a - b;
                break;
            case 'x':
                result = a * b;
                break;
            case '/':
                if (b !== 0) {
                    result = a / b;
                } else {
                    alert('Não é possível dividir por zero');
                    clearAll();
                    return "";
                }
                break;
            default:
                result = b;
        }

        const resultStr = result.toString();
        return resultStr.length > 17 ? resultStr.slice(0, 17) : resultStr;
    }

    function clearAll() {
        firstInput = "";
        secondInput = "";
        operator = "";
        currentOperation = "";
        display.value = "0";
    }

});