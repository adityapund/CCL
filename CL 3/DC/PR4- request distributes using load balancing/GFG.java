import java.rmi.RemoteException;

public class GFG {
    public static int hash_func(int request_id) {
        // Computing the hash request id
        int hashed_id = 112; // Just an example hash value, replace it with your actual hash function
        return hashed_id;
    }

    public static void route_request_to_server(int dest_server) {
        System.out.println("Routing request to the Server ID : " + dest_server);
    }

    public static int request_id = 23; // Incoming Request ID
    public static int server_count = 10; // Total Number of Servers

    public static void main(String args[]) {
        int hashed_id = hash_func(request_id); // Hashing the incoming request id
        int dest_server = hashed_id % server_count; // Computing the destination server id
        route_request_to_server(dest_server);
    }
}
