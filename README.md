# TransportX


flowchart LR
    subgraph Check Statuses
        A(Log Server List) --> B(Get Current Time)
        B --> C(Calculate 15 Minutes Ago)
        C --> D(Log Inside Function)
        D --> E(Loop Through Servers)
        E --> F(Get Modification Date)
        F --> G[File Modified in Past 30 Minutes?]
        G -- Yes --> H(Open Log File)
        H --> I(Read File Contents)
        I --> J(Close File)
        J --> K[Is it Ansible Script?]
        K -- Yes --> L(Split Contents by  # )
        L --> M(Loop Through AnsibleList)
        M --> N[Does it Contain  Stopped ?]
        N -- Yes --> O(Increment Stopped Count)
        N -- No --> M
        M --> P(End Loop)
        P --> Q(Check Stopped Count)
        Q --> R[Greater Than Zero?]
        R -- Yes --> S(Add Server and Full Content to dictResult)
        R -- No --> T(Add Server and  running  to dictResult)
        K -- No --> U[Is it Python or Splus Script?]
        U -- Yes --> V(Check for  Stopped  in Stripped Value)
        V -- Yes --> W(Add Server and Stripped Value to dictResult)
        V -- No --> X(Add Server and  running  to dictResult)
        U -- No --> Y[Is it Cloudify, Javalogs, Sevone, Netbrain Script?]
        Y -- Yes --> Z(Check for  Stopped  in Stripped Value)
        Z -- Yes --> AA(Add Server and Stripped Value to dictResult)
        Z -- No --> BB(Add Server and  running  to dictResult)
        Y -- No --> CC[Is it Camunda Script?]
        CC -- Yes --> DD(Check for  Stopped  in Value)
        DD -- Yes --> EE(Add Server and Stripped Value to dictResult)
        DD -- No --> FF(Add Server and  running  to dictResult)
        CC -- No --> GG(Add Server and  not working - outside time frame  to dictResult)
        F -- No --> HH(File Not Modified in Past 30 Minutes)
        E --> HH
        HH --> II(End Loop)
        II --> JJ(Exception Handling)
        JJ --> KK(Print Exception)
        KK --> LL(Return Results)
    end
