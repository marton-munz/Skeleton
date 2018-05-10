

all:


clean:
    rm -r env

smoketest:
    ./smoketest.sh

unittest:
    pytest test/unit

regtest:
    env/bin/regtest test/regression

test: smoketest unittest regtest


installreqs:


installthis:


install: installreqs installthis



profile: