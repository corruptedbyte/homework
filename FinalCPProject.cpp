#include <iostream>
#include <stdlib.h>
#include <string>
#include <ctime>

using namespace std;

class Character {
    string name;
    int health;
    int strength;
    int speed;

public:
    Character() : name{ "NN" }, health {0}, strength{0}, speed{0} {}
    Character(string na, int he, int st, int sp) : name{ na }, health{ he }, strength{ st }, speed{ sp } {}

    string getName() const {
        return name;
    }
    void showStats() const {
        cout << "Name: " << name << endl << "Health points: " << health << endl << "Strength points: " << strength << endl << "Speed points: " << speed << endl;
    }
    int getHealth() const {
        return health;
    }
    int getStrength() const {
        return health;
    }
    int getSpeed() const {
        return health;
    }
    void setName(string name) {
        this->name = name;
    }
    void setHealth(int health) {
        this->health = health;
    }
    void setStrength(int strength) {
        this->strength = strength;
    }
    void setSpeed(int speed) {
        this->speed = speed;
    }
    void damage(int damagePoints) {
        this->health -= damagePoints;
    }
    void heal(int healthPoints) {
        this->health += healthPoints;
    }
};

class Enemy: public Character {
public:
    Enemy()
    {
        setName("Enemy");
        setHealth(rand() % 100);
        setStrength(rand() % 10);
        setSpeed(rand() % 10);
    }
};
class Us: public Character {
    int gold;
public:
    Us(string name) {
        this->gold = 0;

        setHealth(100);
        setStrength(100);
        setSpeed(rand() % 30);
        setName(name);
    }
    void addGold(int gold) {
        this->gold += gold;
    }
    void spendGold(int gold) {
        this->gold -= gold;
    }
    int getGold() const {
        return gold;
    }
};

int fight(Us& player) {
    Enemy enemy;
    int choice;
    bool defeated;

    system("cls");

    cout << "You've encountered an enemy!" << endl;
    cout << "Enemy strength: " << enemy.getStrength() << endl;
    cout << "Enemy health: " << enemy.getHealth() << endl;

    while (player.getHealth() > 0 || player.getHealth() == 0) {
        while (enemy.getHealth() > 0 || enemy.getHealth() == 0) {
            if (player.getHealth() == 0)
                break;

            cout << "1 - Fight" << endl;
            cout << "2 - Flee" << endl;
            cin >> choice;
            switch (choice) {
            case 1:
                enemy.damage(rand() % player.getStrength());
                player.damage(rand() % enemy.getStrength());

                system("cls");
                cout << "Your Health: " << player.getHealth() << endl;
                cout << "Enemy Health: " << enemy.getHealth() << endl;
                break;
            case 2:
                if (player.getSpeed() > enemy.getSpeed()) {
                    break;
                }
                else {
                    player.damage(rand() % enemy.getStrength());
                    cout << "You couldn't escape so the enemy attacked you!" << endl;
                }
                break;
            }
        }
        if (enemy.getHealth() <= 0) {
            player.addGold(10);
            cout << "You defeated the enemy! +10 gold!";
            system("pause");
            return 0;
        }
    }
    return 0;
}

void menu(Us& player) {
    while (player.getHealth() > 0 || player.getHealth() == 0) {
        int choice = 0;
        cout << "1 - Explore" << endl;
        cout << "2 - View stats" << endl;
        cout << "3 - Shop" << endl;
        cout << "> ";
        cin >> choice;
        cout << endl;

        int addedgold = 0;
        int chance = rand();

        switch (choice) {
            system("cls");
        case 1:
            if (chance >= RAND_MAX / 2) {
                addedgold = rand() % 10;
                player.addGold(addedgold);
                cout << "Awesome! You found " << addedgold << " gold!" << endl;
                system("pause");
            }
            else {
                fight(player);
            }
            break;
        case 2:
            system("cls");
            cout << "Your strength: " << player.getStrength() << endl;
            cout << "Your speed: " << player.getSpeed() << endl;
            cout << "Your health: " << player.getHealth() << endl;
            cout << "Your gold: " << player.getGold() << endl;
            system("pause");
            break;
        case 3:
            if (player.getGold() == 0)
                break;
            choice = 0;
            system("cls");
            cout << "1 - Buy 10 health (5 gold)" << endl;
            cout << "2 - Buy 20 health (10 gold)" << endl;
            cout << "3 - Buy 30 health (15 gold)" << endl;
            cout << "0 - Exit" << endl;
            cin >> choice;
            switch (choice) {
            case 1:
                player.spendGold(5);
                player.heal(10);
                break;
            case 2:
                player.spendGold(10);
                player.heal(20);
                break;
            case 3:
                player.spendGold(15);
                player.heal(30);
                break;
            }
        case 0:
            break;
        }
        system("cls");
    }
}

int main()
{
    srand(time(0));
    cout << "Enter your name: ";
    string name;
    getline(cin, name);
    cout << endl;

    Us mainChar(name);

    menu(mainChar);

    cout << "Your character died!";
}
