function canDriveCar(user,car){
    if (user['age'] >= 18){var correctage = true}
    else {var correctage = false}

    if (car['engineSize'] <= 1000){var correctcc = true}
    else {var correctcc = false}

    if (correctage && correctcc == true) {console.log('you can drive')}
    else {console.log('you cannot drive')}

}
let user1 = {'name':'Jon Doe','age':21}
let car1 = {'engineSize':1200,'name':'Mazda 3'}
canDriveCar(user1,car1)

function areAllNumbersEven(numbers){
    for (let i = 0; i < numbers.length; i++){
    if (numbers[i] %2==0){console.log('even')}
    }
}

const nums = [2,4,6,8]
areAllNumbersEven(nums)

