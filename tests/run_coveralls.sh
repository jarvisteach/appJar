VERS=`python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))'`
if [ "$VERS" = "3.5" ]; then
    echo "Running coveralls"
    coveralls
else
    echo "Not running coveralls - version= $VERS"
fi
