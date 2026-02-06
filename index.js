const balance = document.getElementById('balance');
const income = document.getElementById('income');
const expense = document.getElementById('expense');
const list = document.getElementById('list');
const form = document.getElementById('form');
const text = document.getElementById('text');
const amount = document.getElementById('amount');

let transactions = JSON.parse(localStorage.getItem('transactions')) || [];

function addTransaction(e) {
  e.preventDefault();

  const transaction = {
    id: Date.now(),
    text: text.value,
    amount: +amount.value
  };

  transactions.push(transaction);
  updateLocalStorage();
  updateUI();

  text.value = '';
  amount.value = '';
}

function updateUI() {
  list.innerHTML = '';

  let total = 0, inc = 0, exp = 0;

  transactions.forEach(t => {
    const sign = t.amount < 0 ? '-' : '+';
    const li = document.createElement('li');

    li.innerHTML = `
      ${t.text}
      <span>${sign}₹${Math.abs(t.amount)}</span>
    `;

    list.appendChild(li);

    total += t.amount;
    t.amount > 0 ? inc += t.amount : exp += t.amount;
  });

  balance.innerText = `₹${total}`;
  income.innerText = `₹${inc}`;
  expense.innerText = `₹${Math.abs(exp)}`;
}

function updateLocalStorage() {
  localStorage.setItem('transactions', JSON.stringify(transactions));
}

form.addEventListener('submit', addTransaction);
updateUI();
