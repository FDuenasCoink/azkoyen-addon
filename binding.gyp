{
    "targets": [{
        "target_name": "azkoyen-addon",
        'cflags!': [
            '-fno-exceptions'
        ],
        'cflags_cc!': [
            '-fno-exceptions'
        ],
        'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
        },
        'msvs_settings': {
            'VCCLCompilerTool': {
                'ExceptionHandling': 1
            }
        },
        "sources": [
            "src/main.cpp",
            "src/azkoyen/AzkoyenControl.cpp",
            "src/azkoyen/StateMachine.cpp",
            "src/azkoyen/ValidatorAzkoyen.cpp",
            "src/azkoyen/Azkoyen.cpp",
        ],
        'include_dirs': [
            "<!(node -p \"require('node-addon-api').include_dir\")",
            "src/spdlog/include"
        ],
        'libraries': [],
        'defines': ['NAPI_CPP_EXCEPTIONS'],
        'conditions': [
            ['OS=="mac"', {
            'xcode_settings': {
              'OTHER_CFLAGS': [
                '-arch x86_64',
                '-arch arm64'
              ],
              'OTHER_LDFLAGS': [
                '-framework', 'CoreFoundation',
                '-framework', 'IOKit',
                '-arch x86_64',
                '-arch arm64'
              ],
              'SDKROOT': 'macosx',
              'MACOSX_DEPLOYMENT_TARGET': '10.7'
            }
          }],
        ]
    }]
}