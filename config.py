config = {
    'token' : '<put-your-token-here>',
    'group_id' : 24
}

COOKIES={
    'token': config['token']
}

executes = {
    'cpp17' : '{"final":{"execute":[]},"prepare":{"file":{"source.submission.__SUBMISSION_FILE__":"__SUBMISSION_URL__"},"execute":[{"name":"copy submission source","command":["cp","source.submission.__SUBMISSION_FILE__","__SUBMISSION_FILE__"],"memory_limit":8388608},{"name":"submission.compile","meta":"submission.compile.meta","record":{"stdout":4096,"enable":true,"stderr":4096},"memory_limit":8388608,"stdout":"submission.compile.stdout","command":["g++","__SUBMISSION_FILE__","-o","submission.out","-O2","-std=c++17"],"stderr":"submission.compile.stdout"}]},"tasks":{"execute":[{"name":"copy submission source","command":["cp","source.submission.__SUBMISSION_FILE__","__SUBMISSION_FILE__"],"memory_limit":8388608},{"time_limit":"__TIME_LIMIT__","name":"submission.run.__TASK_ID__","meta":"submission.run.__TASK_ID__.meta","output_limit":"__OUTPUT_LIMIT__","scope":{"import":["__TASK_ID__.stdin","submission.out"],"export":["submission.run.__TASK_ID__.meta","user.__TASK_ID__.stdout"]},"record":{"enable":false},"stdout":"user.__TASK_ID__.stdout","command":["./submission.out"],"stdin":"__TASK_ID__.stdin","memory_limit":"__MEMORY_LIMIT__"}]}}',
    'c11' : '{"final":{"execute":[]},"prepare":{"file":{"source.submission.__SUBMISSION_FILE__":"__SUBMISSION_URL__"},"execute":[{"name":"copy submission source","command":["cp","source.submission.__SUBMISSION_FILE__","__SUBMISSION_FILE__"],"memory_limit":8388608},{"name":"submission.compile","meta":"submission.compile.meta","record":{"stdout":4096,"enable":true,"stderr":4096},"memory_limit":8388608,"stdout":"submission.compile.stdout","command":["gcc","__SUBMISSION_FILE__","-o","submission.out","-lm","-O2","-std=c11"],"stderr":"submission.compile.stdout"}]},"tasks":{"execute":[{"name":"copy submission source","command":["cp","source.submission.__SUBMISSION_FILE__","__SUBMISSION_FILE__"],"memory_limit":8388608},{"time_limit":"__TIME_LIMIT__","name":"submission.run.__TASK_ID__","meta":"submission.run.__TASK_ID__.meta","output_limit":"__OUTPUT_LIMIT__","scope":{"import":["__TASK_ID__.stdin","submission.out"],"export":["submission.run.__TASK_ID__.meta","user.__TASK_ID__.stdout"]},"record":{"enable":false},"stdout":"user.__TASK_ID__.stdout","command":["./submission.out"],"stdin":"__TASK_ID__.stdin","memory_limit":"__MEMORY_LIMIT__"}]}}',
    'java' : '{"final":{"execute":[]},"prepare":{"file":{"source.submission.__SUBMISSION_FILE__":"__SUBMISSION_URL__"},"execute":[{"name":"copy submission source","command":["cp","source.submission.__SUBMISSION_FILE__","__SUBMISSION_FILE__"],"memory_limit":8388608},{"name":"submission.compile","meta":"submission.compile.meta","record":{"stdout":4096,"enable":true,"stderr":4096},"memory_limit":0,"stdout":"submission.compile.stdout","command":["javac","__SUBMISSION_FILE__"],"stderr":"submission.compile.stdout"}]},"tasks":{"execute":[{"name":"copy submission source","command":["cp","source.submission.__SUBMISSION_FILE__","__SUBMISSION_FILE__"],"memory_limit":8388608},{"time_limit":"__TIME_LIMIT__","name":"submission.run.__TASK_ID__","meta":"submission.run.__TASK_ID__.meta","output_limit":"__OUTPUT_LIMIT__","scope":{"import":["__TASK_ID__.stdin","__SUBMISSION_MAIN_FILE__.class"],"export":["submission.run.__TASK_ID__.meta","user.__TASK_ID__.stdout"]},"record":{"enable":false},"stdout":"user.__TASK_ID__.stdout","command":["java","-Xmx__MEMORY_LIMIT__k","-Xss64m","__SUBMISSION_MAIN_FILE__"],"stdin":"__TASK_ID__.stdin","memory_limit":0}]}}',
    'py3' : '{"final":{"execute":[]},"prepare":{"file":{"source.submission.__SUBMISSION_FILE__":"__SUBMISSION_URL__"},"execute":[{"name":"copy submission source","command":["cp","source.submission.__SUBMISSION_FILE__","__SUBMISSION_FILE__"],"memory_limit":8388608},{"name":"submission.compile","meta":"submission.compile.meta","record":{"stdout":4096,"enable":true,"stderr":4096},"memory_limit":8388608,"stdout":"submission.compile.stdout","command":["python3","-m","py_compile","__SUBMISSION_FILE__"],"stderr":"submission.compile.stdout"}]},"tasks":{"execute":[{"name":"copy submission source","command":["cp","source.submission.__SUBMISSION_FILE__","__SUBMISSION_FILE__"],"memory_limit":8388608},{"time_limit":"__TIME_LIMIT__","name":"submission.run.__TASK_ID__","meta":"submission.run.__TASK_ID__.meta","output_limit":"__OUTPUT_LIMIT__","scope":{"import":["__TASK_ID__.stdin","__SUBMISSION_FILE__"],"export":["submission.run.__TASK_ID__.meta","user.__TASK_ID__.stdout"]},"record":{"enable":false},"stdout":"user.__TASK_ID__.stdout","command":["python2","__SUBMISSION_FILE__"],"stdin":"__TASK_ID__.stdin","memory_limit":"__MEMORY_LIMIT__"}]}}',
    'py2' : '{"final":{"execute":[]},"prepare":{"file":{"source.submission.__SUBMISSION_FILE__":"__SUBMISSION_URL__"},"execute":[{"name":"copy submission source","command":["cp","source.submission.__SUBMISSION_FILE__","__SUBMISSION_FILE__"],"memory_limit":8388608},{"name":"submission.compile","meta":"submission.compile.meta","record":{"stdout":4096,"enable":true,"stderr":4096},"memory_limit":8388608,"stdout":"submission.compile.stdout","command":["python2","-m","py_compile","__SUBMISSION_FILE__"],"stderr":"submission.compile.stdout"}]},"tasks":{"execute":[{"name":"copy submission source","command":["cp","source.submission.__SUBMISSION_FILE__","__SUBMISSION_FILE__"],"memory_limit":8388608},{"time_limit":"__TIME_LIMIT__","name":"submission.run.__TASK_ID__","meta":"submission.run.__TASK_ID__.meta","output_limit":"__OUTPUT_LIMIT__","scope":{"import":["__TASK_ID__.stdin","__SUBMISSION_FILE__"],"export":["submission.run.__TASK_ID__.meta","user.__TASK_ID__.stdout"]},"record":{"enable":false},"stdout":"user.__TASK_ID__.stdout","command":["python2","__SUBMISSION_FILE__"],"stdin":"__TASK_ID__.stdin","memory_limit":"__MEMORY_LIMIT__"}]}}'
}
