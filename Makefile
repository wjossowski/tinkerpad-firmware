dir := $(shell pwd)
src := ${dir}/src
libs := ${dir}/3rdparty
out := /Volumes/CIRCUITPY

init: 
	@cp -r ${libs}/kmk_firmware/kmk ${out}
	@cp -r ${libs}/adafruit_display_text ${out}/lib
	@cp ${libs}/adafruit_displayio_ssd1306.mpy ${out}/lib

flash:
	@mkdir -p "${out}/boards"
	@cp ${src}/boards/*.py ${out}/boards
	@mkdir -p "${out}/layers"
	@cp ${src}/layers/*.py ${out}/layers
	@cp -r ${src}/*.py ${out}