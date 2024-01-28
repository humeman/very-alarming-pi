# VeryAlarmingPi

A severely over-engineered alarm clock that runs off of a Raspberry Pi.

## ...Why?
I am a ridiculously heavy sleeper. Even an alarm clock found on Amazon with ear-destroying volumes and bed shaking motors fails to wake me up sometimes.

My goal in this project is to create an alarm clock that **guarantees** I get out of bed in a timely fashion, no matter the circumstances.

## How?
This system has a few features:
* A force-sensitive-resistor, or FSR, which is able to detect when I'm in bed.
* A pair of loud speakers.
* Two mini motorcycle LEDs.
* A bed shaker/vibrating motor.

The idea is when the alarm is set to go off, it starts relatively calm (so as to not wake up my roommates, if at all possible). As it sees that I am still in bed, more and more elements will be turned on (vibration, louder volumes, etc). Eventually, it'll be so unbearable that I have no choice but to stand up.

There is no snooze button. Once it goes off, the only way to stop it (short of smashing it against the floor) is standing up.