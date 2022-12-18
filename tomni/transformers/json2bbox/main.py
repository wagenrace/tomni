from ...shape_fitting.fit_rect_ellipse import fit_rect_around_ellipse

# Optimized by chatGDP
def json2bbox(scf_object: dict) -> tuple:
    if "type" in scf_object:
        if scf_object["type"] == "polygon":
            x_values, y_values = [val["x"] for val in scf_object["points"]], [
                val["y"] for val in scf_object["points"]
            ]
            x_min, y_min, x_max, y_max = (
                min(x_values),
                min(y_values),
                max(x_values),
                max(y_values),
            )
            return (
                int(round(x_min)),
                int(round(y_min)),
                int(round(x_max)),
                int(round(y_max)),
            )
        elif scf_object["type"] in ["circle", "ellipse"]:
            x1, y1, x2, y2 = fit_rect_around_ellipse(
                scf_object["center"]["x"],
                scf_object["center"]["y"],
                scf_object["radiusX"],
                scf_object["radiusY"],
                scf_object["angleOfRotation"],
            )
            return x1, y1, x2, y2
        else:
            # Not given by the AI, it just stopped after `else:`
            raise KeyError(
                f"The scf_object does not have the key 'type'. dict is in the wrong format. {scf_object}"
            )
