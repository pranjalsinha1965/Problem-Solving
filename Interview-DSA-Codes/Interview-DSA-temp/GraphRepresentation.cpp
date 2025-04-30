#include <iostream>
#include <vector>
using namespace std;

int main()
{
    // Part 1: Adjacency Matrix Representation (Undirected Graph)
    {
        int n, m;
        cout << "Adjacency Matrix (Undirected Graph)\n";
        cin >> n >> m;
        int adjMatrix[n + 1][n + 1] = {0};  // Initialize all values to 0

        for(int i = 0; i < m; i++)
        {
            int u, v;
            cin >> u >> v;
            adjMatrix[u][v] = 1;  // Edge from u to v
            adjMatrix[v][u] = 1;  // Edge from v to u (undirected)
        }

        // Print the adjacency matrix
        cout << "Adjacency Matrix:\n";
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                cout << adjMatrix[i][j] << " ";
            }
            cout << endl;
        }
    }

    // Part 2: Adjacency List Representation (Undirected Graph)
    {
        int n, m;
        cout << "Adjacency List (Undirected Graph)\n";
        cin >> n >> m;
        vector<int> adjListUndirected[n + 1];

        for(int i = 0; i < m; i++)
        {
            int u, v;
            cin >> u >> v;
            adjListUndirected[u].push_back(v);  // Edge from u to v
            adjListUndirected[v].push_back(u);  // Edge from v to u (undirected)
        }

        // Print the adjacency list
        cout << "Adjacency List (Undirected):\n";
        for (int i = 1; i <= n; i++) {
            cout << i << ": ";
            for (int j : adjListUndirected[i]) {
                cout << j << " ";
            }
            cout << endl;
        }
    }

    // Part 3: Adjacency List Representation (Directed Graph)
    {
        int n, m;
        cout << "Adjacency List (Directed Graph)\n";
        cin >> n >> m;
        vector<int> adjListDirected[n + 1];

        for(int i = 0; i < m; i++)
        {
            int u, v;
            cin >> u >> v;
            adjListDirected[u].push_back(v);  // Edge from u to v (directed)
        }

        // Print the adjacency list
        cout << "Adjacency List (Directed):\n";
        for (int i = 1; i <= n; i++) {
            cout << i << ": ";
            for (int j : adjListDirected[i]) {
                cout << j << " ";
            }
            cout << endl;
        }
    }

    return 0;
}
