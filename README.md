  Server Load Balancer with MiniNet

# Server Load Balancer with MiniNet

This project implements a server load balancer using MiniNet. It consists of a custom topology with multiple servers, a load balancer, and clients. The system efficiently distributes HTTP requests among multiple servers, ensuring balanced resource usage **based on the Network Utilization of Servers**.

## Features

*   **Custom Topology:** Defined using MiniNet to simulate network components.
* **HTTP Load Balancing:** Implements a load balancer that redirects client requests to servers based on the network link utilization of the server.
*   **Dynamic Status Monitoring:** Monitors server performance and adjusts routing dynamically.
*   **Multi-threaded Servers:** Hosts simple HTTP servers for simulating different types of workloads.
*   **Testing Script:** Simulates client requests to validate the functionality of the load balancer.

## File Structure

*   **topo.py:**
    *   Creates a custom MiniNet topology with:
        *   One switch.
        *   Three servers (`Server_1`, `Server_2`, `Server_3`).
        *   Two clients.
        *   One load balancer.
    *   Sets up the HTTP servers on each host and starts the load balancer.
*   **LoadBalancer/lb.py:**
    *   Implements the load balancer logic.
    *   Forwards client requests to servers based on:
        *   URL path (e.g., large file requests directed to specific servers).
        *   Server status (e.g., load threshold-based redirection).
    *   Logs operations for monitoring.
*   **Request/exe.sh:**
    *   A shell script to simulate HTTP requests from clients.
    *   Sends requests to the load balancer to test various routing scenarios.
*   **Server/server1.py, server2.py, server3.py:**
    *   Implements HTTP servers on the hosts.
    *   Monitors network usage dynamically.
    *   Updates a status file to signal the load balancer about the server's availability.

## Requirements

*   Python 3.x
*   MiniNet
*   psutil (Python library for monitoring system resources)
*   curl (for testing HTTP requests)

## Usage Instructions

1.  **Setup MiniNet Environment:** Ensure MiniNet is installed and configured on your system.
2.  **Run the Topology:**
    
    ```
    sudo python3 topo.py
    ```
    
    This command sets up the network topology and starts the HTTP servers and load balancer.
    
3.  **Execute Client Requests:**
    
    ```
    bash exe.sh
    ```
    
    Simulates multiple client requests to test the load balancer.
    
4.  **Monitor Logs:**
    *   Load balancer logs: `lb.log`
    *   Server logs: `Server/logging`.

## How It Works

1.  **Topology Initialization:**
    *   `topo.py` defines and launches the network.
    *   Servers and the load balancer are started on their respective hosts.
2.  **Request Handling:**
    *   Clients send requests to the load balancer's IP (`10.0.0.254`).
    *   The load balancer forwards the requests to an appropriate server based on:
        *   Server load (monitored using `psutil`).
        *   URL path (specific files are routed to specific servers).
3.  **Dynamic Load Monitoring:**
    *   Each server updates its status based on network utilization.
    *   The load balancer uses these updates to make routing decisions.


This project demonstrates a practical application of MiniNet in designing and testing network systems. It serves as a foundation for more complex load-balancing and network simulation experiments.
