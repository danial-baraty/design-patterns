import threading
import time

class BankAccountManagerSingleton:
    """
    BankAccountManagerSingleton ensures only one instance exists in the system.
    
    Why Singleton?
    - We need a shared lock manager for all accounts.
    - If multiple instances existed, each would maintain its own lock dictionary.
      That means two different managers could both operate on the same account
      without knowing the other already locked it -> race condition and data corruption.
    """
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.locks = {}
            return cls._instance

    def deposit(self, account_id, amount):
        if self.locks.get(account_id):
            print(f"[{threading.current_thread().name}] Account {account_id} locked. Skipped.")
            return
        print(f"[{threading.current_thread().name}] Locking {account_id} for deposit.")
        self.locks[account_id] = True
        time.sleep(1)  # simulate transaction
        print(f"[{threading.current_thread().name}] Deposited {amount} to {account_id}.")
        del self.locks[account_id]

    def withdraw(self, account_id, amount):
        if self.locks.get(account_id):
            print(f"[{threading.current_thread().name}] Account {account_id} locked. Skipped.")
            return
        print(f"[{threading.current_thread().name}] Locking {account_id} for withdraw.")
        self.locks[account_id] = True
        time.sleep(1)  # simulate transaction
        print(f"[{threading.current_thread().name}] Withdrew {amount} from {account_id}.")
        del self.locks[account_id]


# Both references point to the same singleton instance
atm_manager = BankAccountManagerSingleton()
mobile_app_manager = BankAccountManagerSingleton()

def atm_deposit_task():
    atm_manager.deposit('acct_12345', 100)

def mobile_withdraw_task():
    mobile_app_manager.withdraw('acct_12345', 50)

# Simulate ATM and Mobile App accessing the same account concurrently
t1 = threading.Thread(target=atm_deposit_task, name="ATM-Thread")
t2 = threading.Thread(target=mobile_withdraw_task, name="MobileApp-Thread")

t1.start()
t2.start()
t1.join()
t2.join()
