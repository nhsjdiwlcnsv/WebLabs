class Employee {
    constructor(fullName, age, department) {
        this._fullName = fullName;
        this._age = age;
        this._department = department;
    }

    get fullName() {
        return this._fullName;
    }

    set fullName(value) {
        this._fullName = value;
    }

    get age() {
        return this._age;
    }

    set age(value) {
        this._age = value;
    }

    get department() {
        return this._department;
    }

    set department(value) {
        this._department = value;
    }

    toString = isAgeValid(() => {
        return `${this.fullName}, ${this.age}, works at ${this.department} department`;
    })
}

class Tailor extends Employee {
    constructor(fullName, age, salary) {
        super(fullName, age, 'Tailorship');
        this._salary = salary;
    }

    get salary() {
        return this._salary;
    }

    set salary(value) {
        this._salary = value;
    }

    toString() {
        return `${super.toString()}, and makes $${this.salary} monthly`;
    }
}


function isAgeValid(func) {
    function wrapper(params) {
        const maxAge = 75
        const minAge = 18

        const isAgeValid = this.age >= minAge && this.age <= maxAge

        alert(`${this.fullName} (${this.age}) is ${isAgeValid ? '' : 'not'} eligible to work here.`)

        return func.apply(this, params)
    }

    return wrapper
}

const tailor = new Tailor('Ab\'Oba', 48, 5000);

alert(tailor.toString())
alert(tailor.fullName)
alert(tailor.age)
alert(tailor.department)
alert(tailor.salary)

tailor.fullName = 'Ah\'Uha';
tailor.age = 99;
tailor.salary = 9185;

console.log("ASDADASD")

alert(tailor.toString())
alert(tailor.fullName)
alert(tailor.age)
alert(tailor.department)
alert(tailor.salary)


// function Employee(fullName, age, department) {
//     let _fullName = fullName;
//     let _age = age;
//     let _department = department;
//
//     this.fullName = (fullName) => {
//         if (fullName === undefined)
//             return _fullName;
//         else _fullName = fullName
//     }
//
//     this.age = (age) => {
//         if (age === undefined)
//             return _age;
//         else _age = age
//     }
//
//     this.department = (department) => {
//         if (department === undefined)
//             return _department;
//         else _department = department
//     }
//
//     this.toString = () =>
//         `${this.fullName}, ${this.age}, works at ${this.department} department`;
// }
//
// function Tailor(fullName, age, department, salary) {
//     let _salary = salary;
//
//     this.__proto__ = new Employee(fullName, age, department);
//
//     this.salary = (salary) => {
//         if (salary === undefined)
//             return _salary;
//         else _salary = salary
//     }
//
//     toString = () =>
//         `${this.fullName}, ${this.age}, works at ${this.department} department, and makes $${this.salary} monthly`
//
// }