class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550
        self.buy = False
        self.open = True

    def user_input(self, command):
        if command.isalpha():
            if command == 'fill':
                coffee_machine.fill()
            elif command == 'take':
                coffee_machine.take()
            elif command == 'remaining':
                coffee_machine.display_status()
            # elif command == 'back':
            #     return 'continue'
            elif command == 'exit':
                self.open = False
            else:
                self.buy = True
        else:
            drink = int(command)
            if drink == 1:
                self.espresso()
            elif drink == 2:
                self.latte()
            elif drink == 3:
                self.capuccino()



    def espresso(self):
        if self.resource_check(250, 0, 16):
            self.water -= 250
            self.coffee -= 16
            self.money += 4
            self.cups -= 1
            self.buy = False

    def latte(self):
        if self.resource_check(350, 75, 20):
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.money += 7
            self.cups -= 1
            self.buy = False

    def capuccino(self):
        if self.resource_check(200, 100, 12):
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.money += 6
            self.cups -= 1
            self.buy = False

    def resource_check(self, water, milk, coffee):
        missing = []
        if self.water - water < 0:
            missing.append('water')
        if self.milk - milk < 0:
            missing.append('milk')
        if self.coffee - coffee < 0:
            missing.append('coffee')
        if self.cups - 1 <= 0:
            missing.append('cup')
        if missing:
            print(f'Sorry, not enough {", ".join(missing)}!')
            return False
        print('I have enough resources, making you a coffee!')
        return True



    def fill(self):
        print('Write how many ml of water you want to add:')
        self.water += int(input())
        print('Write how many ml of milk you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee you want to add:')
        self.coffee += int(input())
        print('Write how many disposable cups you want to add:')
        self.cups += int(input())
        return self

    def take(self):
        self.money = 0
        return self

    def display_status(self):
        print('This coffee machine has:')
        print(f'{self.water} ml of water')
        print(f'{self.milk} ml of milk')
        print(f'{self.coffee} g of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'${self.money} of money')


coffee_machine = CoffeeMachine()
while coffee_machine.open:
    option = input('Write action (buy, fill, take, remaining, exit):')
    coffee_machine.user_input(option)
    if coffee_machine.buy:
        option = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        coffee_machine.user_input(option)