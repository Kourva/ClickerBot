from pyscript import window, document, display

def add_balacne(event):
    energy_value = document.querySelector("#energy_value")
    energy_left = document.querySelector("#energy_progress_left")

    progress_value = document.querySelector("#energy_progress")    
    coin_balance = document.querySelector("#coin_balance")
    power_value = document.querySelector("#power_value").innerHTML

    if int(energy_left.innerHTML) > 0:
        coin_balance.innerHTML = str(
            int(coin_balance.innerHTML) + int(power_value)
        )
        energy_left.innerHTML = str(
            int(energy_left.innerHTML) - 1
        )
        percentage = int(
            int(energy_left.innerHTML) / int(energy_value.innerHTML) * 100
        )
        progress_value.value = str(percentage)

    window.navigator.vibrate(50)

def upgrade_tap(event):
    balance_value = int(document.querySelector("#coin_balance").innerHTML)

    power_level = int(document.querySelector("#power_level").innerHTML)
    power_value = int(document.querySelector("#power_value").innerHTML)
    power_money = int(document.querySelector("#power_money").innerHTML)

    if balance_value >= power_money:
        balance_value -= power_money
        power_level += 1
        power_value += 1
        power_money = 2**power_level

        document.querySelector("#coin_balance").innerHTML = str(balance_value)
        document.querySelector("#power_level").innerHTML = str(power_level)
        document.querySelector("#power_value").innerHTML = str(power_value)
        document.querySelector("#power_money").innerHTML = str(power_money)
        
    else:
        window.navigator.vibrate(200)
        window.alert("Not enough balance to upgrade power")

def upgrade_energy(event):
    balance_value = int(document.querySelector("#coin_balance").innerHTML)

    energy_value = document.querySelector("#energy_value")
    energy_left = document.querySelector("#energy_progress_left")
    progress_value = document.querySelector("#energy_progress")  

    energy_level = int(document.querySelector("#energy_level").innerHTML)
    energy_value = int(document.querySelector("#energy_value").innerHTML)
    energy_money = int(document.querySelector("#energy_money").innerHTML)

    if balance_value >= energy_money:
        balance_value -= energy_money
        energy_level += 1
        energy_value += 500
        energy_money = 2**energy_level

        percentage = int(
            int(energy_left.innerHTML) / int(energy_value) * 100
        )
        progress_value.value = str(percentage)

        document.querySelector("#coin_balance").innerHTML = str(balance_value)
        document.querySelector("#energy_level").innerHTML = str(energy_level)
        document.querySelector("#energy_value").innerHTML = str(energy_value)
        document.querySelector("#energy_money").innerHTML = str(energy_money)
        
    else:
        window.navigator.vibrate(200)
        window.alert("Not enough balance to upgrade energy")
