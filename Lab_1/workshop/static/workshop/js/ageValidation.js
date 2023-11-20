const ageInput = document.getElementById('age');

const daysOfWeek = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]

// Функция для проверки, является ли строка корректной датой
const isValidDate = (str) => {
  const date = new Date(str);
  return !isNaN(date);
};

// Функция для вычисления возраста пользователя в годах
const getAge = (str) => {
  const birthDate = new Date(str);
  const currentDate = new Date();
  const diff = currentDate - birthDate;

  return Math.floor(diff / (1000 * 60 * 60 * 24 * 365));
};

// Функция для получения дня недели из даты
const getDayOfWeek = (str) => {
  const date = new Date(str);
  const day = date.getDay();

  return daysOfWeek[day];
};

// Добавляем обработчик события потери фокуса для поля ввода даты
ageInput.addEventListener('blur', (e) => {
  const value = e.target.value;
  if (isValidDate(value)) {
    const age = getAge(value);
    if (age >= 18) {
      const day = getDayOfWeek(value);
      alert(`Ah, you are in your prime; you've come of age! You're ${age} years young and your day is ${day}.`);
    } else {
      alert('STAY BACK LIL SNICKER!');
    }
  } else {
    alert('Errmmm... Dude.. what the flip?');
  }
});