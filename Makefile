smoketest:
    test/smoke/test_installation.sh

test: smoketest

clean:
    rm -rf env