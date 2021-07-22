public class TransactExample {
    public void base_ok(Transaction t) {
        // OK: verify called before make
        verify_transaction(t);
        make_transaction(t);
    }
    
    public void no_verify(Transaction t) {
        // BAD: transaction isn’t verified
        make_transaction(t);
    }

    public void late_verify(Transaction t){
        // BAD: transaction verified after being made
        make_transaction(t);
        verify_transaction(t);
    }
}