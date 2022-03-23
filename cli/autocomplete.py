ac_table = {
    'commands': [
        '--help',
        '--version',
        '--version-full',
        'hello',
        'executor',
        'flow',
        'ping',
        'new',
        'gateway',
        'hub',
        'help',
        'pod',
        'deployment',
        'client',
        'export-api',
    ],
    'completions': {
        'hello fashion': [
            '--help',
            '--workdir',
            '--download-proxy',
            '--index-data-url',
            '--index-labels-url',
            '--query-data-url',
            '--query-labels-url',
            '--num-query',
            '--top-k',
        ],
        'hello chatbot': [
            '--help',
            '--workdir',
            '--download-proxy',
            '--index-data-url',
            '--port',
            '--replicas',
            '--unblock-query-flow',
        ],
        'hello multimodal': [
            '--help',
            '--workdir',
            '--download-proxy',
            '--index-data-url',
            '--port',
            '--unblock-query-flow',
        ],
        'hello fork': ['--help', 'fashion', 'chatbot', 'multimodal'],
        'hello': ['--help', 'fashion', 'chatbot', 'multimodal', 'fork'],
        'executor': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--workspace-id',
            '--extra-search-paths',
            '--timeout-ctrl',
            '--k8s-namespace',
            '--polling',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--host-in',
            '--native',
            '--output-array-type',
            '--entrypoint',
            '--docker-kwargs',
            '--pull-latest',
            '--volumes',
            '--gpus',
            '--host',
            '--port-jinad',
            '--quiet-remote-logs',
            '--upload-files',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--shard-id',
            '--pod-role',
            '--noblock-on-start',
            '--shards',
            '--replicas',
            '--port',
            '--install-requirements',
            '--force-update',
            '--force',
            '--compression',
            '--uses-before-address',
            '--uses-after-address',
            '--connection-list',
            '--disable-reduce',
        ],
        'flow': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--workspace-id',
            '--extra-search-paths',
            '--timeout-ctrl',
            '--k8s-namespace',
            '--polling',
            '--expose-graphql-endpoint',
            '--uses',
            '--env',
            '--inspect',
        ],
        'ping': ['--help', '--timeout', '--retries'],
        'new': ['--help'],
        'gateway': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--workspace-id',
            '--extra-search-paths',
            '--timeout-ctrl',
            '--k8s-namespace',
            '--polling',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--host-in',
            '--native',
            '--output-array-type',
            '--prefetch',
            '--title',
            '--description',
            '--cors',
            '--default-swagger-ui',
            '--no-debug-endpoints',
            '--no-crud-endpoints',
            '--expose-endpoints',
            '--uvicorn-kwargs',
            '--grpc-server-kwargs',
            '--ssl-certfile',
            '--ssl-keyfile',
            '--expose-graphql-endpoint',
            '--protocol',
            '--host',
            '--proxy',
            '--port-expose',
            '--graph-description',
            '--graph-conditions',
            '--deployments-addresses',
            '--compression',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--shard-id',
            '--pod-role',
            '--noblock-on-start',
            '--shards',
            '--replicas',
            '--port',
            '--uses-before-address',
            '--uses-after-address',
            '--connection-list',
            '--disable-reduce',
        ],
        'hub new': [
            '--help',
            '--name',
            '--path',
            '--advance-configuration',
            '--description',
            '--keywords',
            '--url',
            '--add-dockerfile',
        ],
        'hub push': [
            '--help',
            '--no-usage',
            '--verbose',
            '--dockerfile',
            '--tag',
            '--force-update',
            '--force',
            '--secret',
            '--public',
            '--private',
        ],
        'hub pull': [
            '--help',
            '--no-usage',
            '--install-requirements',
            '--force-update',
            '--force',
        ],
        'hub': ['--help', 'new', 'push', 'pull'],
        'help': ['--help'],
        'pod': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--workspace-id',
            '--extra-search-paths',
            '--timeout-ctrl',
            '--k8s-namespace',
            '--polling',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--host-in',
            '--native',
            '--output-array-type',
            '--entrypoint',
            '--docker-kwargs',
            '--pull-latest',
            '--volumes',
            '--gpus',
            '--host',
            '--port-jinad',
            '--quiet-remote-logs',
            '--upload-files',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--shard-id',
            '--pod-role',
            '--noblock-on-start',
            '--shards',
            '--replicas',
            '--port',
            '--install-requirements',
            '--force-update',
            '--force',
            '--compression',
            '--uses-before-address',
            '--uses-after-address',
            '--connection-list',
            '--disable-reduce',
        ],
        'deployment': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--workspace-id',
            '--extra-search-paths',
            '--timeout-ctrl',
            '--k8s-namespace',
            '--polling',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--host-in',
            '--native',
            '--output-array-type',
            '--entrypoint',
            '--docker-kwargs',
            '--pull-latest',
            '--volumes',
            '--gpus',
            '--host',
            '--port-jinad',
            '--quiet-remote-logs',
            '--upload-files',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--shard-id',
            '--pod-role',
            '--noblock-on-start',
            '--shards',
            '--replicas',
            '--port',
            '--install-requirements',
            '--force-update',
            '--force',
            '--compression',
            '--uses-before-address',
            '--uses-after-address',
            '--connection-list',
            '--disable-reduce',
            '--uses-before',
            '--uses-after',
            '--when',
            '--external',
            '--deployment-role',
        ],
        'client': [
            '--help',
            '--host',
            '--proxy',
            '--port',
            '--tls',
            '--https',
            '--asyncio',
            '--return-responses',
            '--protocol',
        ],
        'export-api': ['--help', '--yaml-path', '--json-path', '--schema-path'],
    },
}
