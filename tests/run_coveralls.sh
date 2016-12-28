VERS=`python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))'`
if [ "$VERS" = "3.5" ]; then
    echo "Running coveralls"
    coveralls
    codeclimate-test-reporter
    CODECLIMATE_REPO_TOKEN=3b1c31ab1ba5ee5eb7aaf75efd1245ee00e38a070f7a82fece4b5f7b9ca5f7f7 codeclimate-test-reporter
else
    echo "Not running coveralls - version= $VERS"
fi
