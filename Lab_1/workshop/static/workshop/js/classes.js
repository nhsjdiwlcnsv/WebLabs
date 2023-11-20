class Employee {
    constructor(fullName, age, department) {
        this._fullName = fullName
        this._age = age
        this._department = department
    }

    fullName(fullName) {
        if (fullName === undefined)
            return this._fullName
        else
            this._fullName = fullName
    }

    age(age) {
        if (age === undefined)
            return this._age
        else
            this._age = age
    }

    department(department) {
        if (department === undefined)
            return this._department
        else
            this._department = department
    }

    toString = () =>
        `${this.fullName()}, ${this.age()}, works at ${this.department()} department`
}


class Tailor extends Employee {
    constructor(fullName, age, salary) {
        super(fullName, age, 'Tailorship');
        this._salary = salary
    }

    salary(salary) {
        if (salary === undefined)
            return this._salary
        else
            this._salary = salary
    }

    toString = () =>
        `${this.fullName()}, ${this.age()}, works at ${this.department()} department, and makes $${this.salary()} monthly`

    toString = isAgeValid(this.age)

}


function isAgeValid(func) {
    function wrapper(params) {
        const maxAge = 75
        const minAge = 18

        const isAgeValid = this.age() >= minAge && this.age() <= maxAge

        alert(`${this.fullName()} (${this.age()}) is ${isAgeValid ? '' : 'not'} eligible to work here.`)

        return func.apply(this, params)
    }

    return wrapper
}

const tailor = new Tailor('Ab\'Oba', 48, 5000);

alert(tailor.toString())
alert(tailor.fullName())
alert(tailor.age())
alert(tailor.department())
alert(tailor.salary())

tailor.fullName('Ah\'Uha');
tailor.age(99);
tailor.salary(9185);

alert(tailor.toString())
alert(tailor.fullName())
alert(tailor.age())
alert(tailor.department())
alert(tailor.salary())