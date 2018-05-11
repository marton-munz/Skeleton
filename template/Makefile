

all:


clean:
    rm -r env

smoketest:
    test/smoke/test_installation.sh

unittest:
    pytest test/unit

regtest:
    env/bin/regtest test/regression

test: smoketest unittest regtest


installreqs:


installthis:


install: installreqs installthis



profile: