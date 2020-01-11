# DEFN 10 ST=RECD,RT=;Latitude:f12.7:UNIT=deg:NULL=-99.9999999,NAME=Latitude:DATUM=GDA94
# DEFN 11 ST=RECD,RT=;Longitude:f13.7:UNIT=deg:NULL=-999.9999999,NAME=Longitude:DATUM=GDA94


def load_aem_points():

    data_points = []
    lines = set()

    with open("data/AusAEM_Year1_NT_Final_CND.dat") as nt_aem_file:

        for idx, l in enumerate(nt_aem_file.readlines()):

            # if idx > 200:
            #     break

            toks = l.split()
            line = int(toks[0])
            lat = float(toks[10])
            lon = float(toks[11])

            cdi_slices = list(map(float, toks[221:]))

            pt = (line, lon, lat, *cdi_slices)
            data_points.append(pt)

            lines.add(line)

    print(len(data_points))
    print(len(lines))

    return data_points, lines


if __name__ == '__main__':
    load_aem_points()