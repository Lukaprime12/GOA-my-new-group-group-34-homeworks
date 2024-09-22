const ironman = {
    realname: 'Tony',
    money: '80 billion',
    roles: 'Genius billionaire playboy philanthropist',
    surname: 'stark',
    protagonist: true,
}

ironman.money = '8 cents';

console.log(ironman.realname);
console.log(ironman.money);
console.log(ironman.roles);
console.log(ironman.surname);

delete ironman.protagonist;
ironman.surname = 'Stark'

console.log(ironman.realname);
console.log(ironman.money);
console.log(ironman.surname);
console.log(ironman.roles);